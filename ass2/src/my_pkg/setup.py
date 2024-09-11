from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools', 'cus_pkg'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A package for harvest scheduling system.',
    entry_points={
        'console_scripts': [
            'server = my_pkg.server:main',  # Ensure this matches your main function
            'client = my_pkg.client:main',    # Ensure you have this for the client
        ],
    },
)

