import pygame

import globals
import objects
import marble_class
import track_class

# --- Constants ---
# No gravity, but we keep bounciness for wall/marble hits
BOUNCINESS = 1.0  # 1.0 = perfectly elastic (no energy lost)

def get_distance_from_line_segment(point: pygame.Vector2, line_start: pygame.Vector2, line_end: pygame.Vector2) -> float:
    line_vec = line_end - line_start
    point_vec = point - line_start
    
    line_len_sq = line_vec.length_squared()
    
    if line_len_sq == 0:
        return point.distance_to(line_start)
    
    t = point_vec.dot(line_vec) / line_len_sq
    t = max(0, min(1, t))
    
    closest_point = line_start + (line_vec * t)
    return point.distance_to(closest_point)

def main():

    # 1. Sort objects into lists for easier processing
    tracks: list[track_class.track] = []
    marbles: list[marble_class.marble] = []

    for ID, object in objects.getAll().items():
        if type(object) is track_class.track:
            tracks.append(object)
        elif type(object) is marble_class.marble:
            marbles.append(object)

    # 2. Physics Step
    for marble in marbles:

        # --- A. Marble vs Track Collision ---
        for track in tracks:
            num_corners = len(track.corners)
            for j in range(num_corners):
                corner1 = track.corners[j]
                corner2 = track.corners[(j + 1) % num_corners]

                dist = get_distance_from_line_segment(marble.position, corner1, corner2)

                if dist <= marble.radius:
                    wall_vec = corner2 - corner1
                    if wall_vec.length_squared() == 0: continue

                    # Calculate normal
                    line_len_sq = wall_vec.length_squared()
                    t = (marble.position - corner1).dot(wall_vec) / line_len_sq
                    t = max(0, min(1, t))
                    
                    closest_point = corner1 + (wall_vec * t)
                    collision_normal = marble.position - closest_point
                    
                    if collision_normal.length_squared() == 0:
                        collision_normal = pygame.Vector2(-wall_vec.y, wall_vec.x)
                    collision_normal = collision_normal.normalize()

                    # Position Correction (Push out of wall)
                    overlap = marble.radius - dist
                    marble.position += collision_normal * (overlap + 0.1)

                    # Velocity Reflection
                    if marble.velocity.dot(collision_normal) < 0:
                        marble.velocity = marble.velocity.reflect(collision_normal) * BOUNCINESS

    # --- B. Marble vs Marble Collision ---
    # We use a nested loop to check every unique pair (e.g. 1vs2, but not 2vs1 again)
    for i in range(len(marbles)):
        for j in range(i + 1, len(marbles)):
            m1 = marbles[i]
            m2 = marbles[j]

            delta = m1.position - m2.position
            dist = delta.length()
            min_dist = m1.radius + m2.radius

            if dist < min_dist:
                # 1. Resolve Position (Push them apart so they don't stick)
                overlap = min_dist - dist
                
                if dist == 0: # Edge case: exact same position
                    normal = pygame.Vector2(1, 0)
                else:
                    normal = delta.normalize()
                
                # Move each marble half the overlap distance away from the center
                push_vector = normal * (overlap * 0.5)
                m1.position += push_vector
                m2.position -= push_vector

                # 2. Resolve Velocity (Elastic Collision)
                # Calculate relative velocity
                rel_vel = m1.velocity - m2.velocity
                vel_along_normal = rel_vel.dot(normal)

                # Only resolve if they are moving towards each other
                if vel_along_normal < 0:
                    # Impulse scalar (Assuming equal mass for simplicity)
                    # j = -(1 + e) * vel_along_normal / (1/m1 + 1/m2)
                    # If mass is 1 for both, divisor is 2.
                    j = -(1 + BOUNCINESS) * vel_along_normal / 2

                    impulse = normal * j
                    m1.velocity += impulse
                    m2.velocity -= impulse

    # 3. Final Movement
    for marble in marbles:
        marble.position += marble.velocity

if __name__ == "__main__":
    main()