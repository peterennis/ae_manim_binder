%%manim -qm -v WARNING Label3DAxes
# Magic for use in Jupyter Notebook

from manim import *

class Label3DAxes(ThreeDScene):
    def construct(self):
        # Make XY plane like 2D: X right, Y up, Z out of screen:
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        # phi = 0 → no tilt (we’re in the XY plane)
        # theta = -90° → rotates the camera so X points right, Y up, and Z comes out

        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=4, y_length=4, z_length=4
        ).add_coordinates()
        self.add(axes)

        # Labels placed just outside the axes ticks:
        x_label = MathTex("X").scale(1.2).move_to(axes.c2p(2.5, 0, 0))
        y_label = MathTex("Y").scale(1.2).move_to(axes.c2p(0, 2.5, 0))
        z_label = MathTex("Z").scale(1.2).move_to(axes.c2p(0, 0, 2.5))

        # Tell the 3D camera/scene to keep these mobjects with fixed orientation
        # (the right API for v0.19.0)
        self.add_fixed_orientation_mobjects(x_label, y_label, z_label)
        self.add(x_label, y_label, z_label)

        # Reference cube:
        cube = Cube(side_length=2).move_to(axes.c2p(0, 0, 0))
        self.add(cube)

        # Choose the rotation you want:
        # Rotate around Z axis (depth)
        self.begin_ambient_camera_rotation(rate=0.2, about='gamma')
        self.wait(8)
        self.stop_ambient_camera_rotation()
