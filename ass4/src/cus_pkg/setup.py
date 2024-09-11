from setuptools import setup

package_name = 'cus_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
        [f'resource/{package_name}']),
        ('share/{package_name}',
        ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='ROS 2 package for cleaning robot task management.',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = cus_pkg.client:main',
            'server = cus_pkg.server:main',
        ],
    },
)

