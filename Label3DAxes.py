# Magic for use in Jupyter Notebook
# %%manim -qm -v WARNING Label3DAxes

from manim import *

class Label3DAxes(ThreeDScene):
    def construct(self):
        # Set camera so XY plane is front-facing, Z comes out
        #self.set_camera_orientation(phi=0 * DEGREES, theta=90 * DEGREES)

        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[-2.5, 2.5, 1],
            x_length=5,
            y_length=5,
            z_length=5
        ).add_coordinates()
        self.add(axes)

        # Create MathTex labels
        x_label = MathTex("X").scale(1.2).move_to(axes.c2p(2.75, 0, 0))
        y_label = MathTex("Y").scale(1.2).move_to(axes.c2p(0, 2.75, 0))
        z_label = MathTex("Z").scale(1.2).move_to(axes.c2p(0, 0, 2.75))

        # Save original orientation to prevent spinning
        for label in [x_label, y_label, z_label]:
            label.save_state()

        def face_camera(label):
            label.restore()
            label.rotate(-self.camera.get_phi(), axis=RIGHT)
            label.rotate(-self.camera.get_theta(), axis=UP)

        for label in [x_label, y_label, z_label]:
            label.add_updater(face_camera)
            self.add(label)

        # Add a cube for spatial reference
        cube = Cube(side_length=2).move_to(axes.c2p(0, 0, 0))
        self.add(cube)

        # Rotate around Z axis (depth)
        self.begin_ambient_camera_rotation(rate=0.2, about="gamma")
        self.wait(8)
        self.stop_ambient_camera_rotation()
