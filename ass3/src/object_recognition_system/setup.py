from setuptools import setup

package_name = 'object_recognition_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Object Recognition and Grasping System',
    license='License Declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_node = object_recognition_system.vision_node:main',
            'robotic_arm_node = object_recognition_system.robotic_arm_node:main',
        ],
    },
)

