from setuptools import setup

package_name = 'hello_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eric',
    maintainer_email='epiraux@gmail.com',
    description='my first hello world for ROS',
    license='Gnou-Girafe-Bug licence (c)2099',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = hello_py_pkg.publisher:main',
            'subscriber = hello_py_pkg.subscriber:main'
        ],
    },
)
