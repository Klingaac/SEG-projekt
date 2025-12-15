import numpy as np
import matplotlib.path as mpltPath

# Polygon vertices (Your vec2 list, e.g., corners of a track)
# Must be in the format: [[x1, y1], [x2, y2], ...]
polygon_vertices = np.array([
    [100, 100], [200, 50], [300, 100], [200, 200]
])

# The point to check (Your marble position)
test_point = (150, 150) 

# Create the Path object (do this once for the polygon)
poly_path = mpltPath.Path(polygon_vertices)

# Check if the point is contained (do this every frame)
is_inside = poly_path.contains_point(test_point) 

print(f"Point {test_point} is inside: {is_inside}")