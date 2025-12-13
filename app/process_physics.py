import pygame

import globals
import objects
import marble_class
import track_class

def main():

    tracks: list[track_class.track] = []
    
    for ID, object in objects.getAll().items():
        if type(object) is track_class.track:
            tracks.append(object)

    for ID, object in objects.getAll().items():

        # marble physics
        # 90 percent made by gemini
        if type(object) is marble_class.marble:

            for i, track in enumerate(tracks):

                for j in range(4):

                    corner1 = track.corners[j]
                    corner2 = track.corners[(j + 1) % len(track.corners)]

                    dist = get_distance_from_line_segment(object.position, corner1, corner2)

                    if dist <= object.radius:
                        
                        # 2. Calculate the Wall Vector and Normal
                        wall_vec = corner2 - corner1
                        if wall_vec.length_squared() == 0: continue # skip zero-length edges
                        
                        # We need the exact point on the line to calculate the normal correctly
                        # (Re-calculating t here similar to your helper function)
                        line_len_sq = wall_vec.length_squared()
                        t = (object.position - corner1).dot(wall_vec) / line_len_sq
                        t = max(0, min(1, t))
                        
                        closest_point = corner1 + (wall_vec * t)
                        
                        # 3. Calculate Collision Normal
                        # The normal is the direction FROM the wall TO the ball
                        collision_normal = object.position - closest_point
                        
                        # If the ball is exactly on the line, normal is (0,0), which breaks math.
                        # We fallback to perpendicular of wall_vec
                        if collision_normal.length_squared() == 0:
                            # rotate wall vector 90 degrees
                            collision_normal = pygame.Vector2(-wall_vec.y, wall_vec.x) 
                        
                        collision_normal = collision_normal.normalize()

                        # 4. POSITION CORRECTION (Crucial to stop sticking!)
                        # Push the ball out of the wall so it's no longer overlapping
                        overlap = object.radius - dist
                        # Push slightly more (1.001) to ensure floating point safety
                        object.position += collision_normal * (overlap + 0.1)

                        # 5. VELOCITY REFLECTION
                        # Pygame has a built-in reflect function!
                        # We only reflect if the ball is actually moving INTO the wall.
                        # (Dot product < 0 means they are opposing)
                        if object.velocity.dot(collision_normal) < 0:
                            
                            # Optional: Bounciness factor (elasticity)
                            # 1.0 = perfect bounce, 0.5 = loses energy
                            bounciness = 1
                            
                            object.velocity = object.velocity.reflect(collision_normal) * bounciness
                        continue

            object.position += object.velocity



# by gemini
def get_distance_from_line_segment(point: pygame.Vector2, line_start: pygame.Vector2, line_end: pygame.Vector2) -> float:
    line_vec = line_end - line_start
    point_vec = point - line_start
    
    # Calculate length squared to avoid unnecessary square roots
    line_len_sq = line_vec.length_squared()
    
    # Edge case: line_start and line_end are the same point
    if line_len_sq == 0:
        return point.distance_to(line_start)
    
    # Calculate the scalar projection (t) of the point onto the line
    # t represents the ratio of the distance along the line (0.0 to 1.0)
    t = point_vec.dot(line_vec) / line_len_sq
    
    # Clamp t to the segment [0, 1] to handle the "segment" logic
    # If you want an INFINITE line, remove the max/min clamping
    t = max(0, min(1, t))
    
    # Find the closest point on the line segment
    closest_point = line_start + (line_vec * t)
    
    # Return the distance between the point and the closest spot
    return point.distance_to(closest_point)
