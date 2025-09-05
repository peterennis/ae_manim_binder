######################################################################
# 📐 3D Geometric Solids
# Available in manim.mobject.three_d.three_dimensions:
# Cube
# Prism
# Octahedron
# Tetrahedron
# Dodecahedron
# Icosahedron
# Polyhedron (base class for custom solids)
# 
# 🌐 Curves & Surfaces
# Available in manim.mobject.three_d.three_dimensions and manim.mobject.three_d.shapes:
# Sphere
# Cylinder
# Cone
# Line3D
# Arrow3D
# Torus
# ThreeDAxes
# ParametricSurface
# Surface
######################################################################

%%manim -qm Show3DObjects

from manim import *

class Show3DObjects(ThreeDScene):
    def construct(self):
        # Set the camera orientation
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)

        # Create 3D mobjects
        cube = Cube()
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.5).shift(RIGHT*3)
        cone = Cone().shift(LEFT*3)
        axes = ThreeDAxes()

        # Add them to the scene
        self.add(axes, cube, sphere, cone)
        self.play(Rotate(axes, PI), Rotate(cube, PI), Rotate(sphere, PI), Rotate(cone, PI), run_time=3)
        