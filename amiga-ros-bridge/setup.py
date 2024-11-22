from setuptools import setup, find_packages

package_name = 'amiga-ros-bridge'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[
        'rclpy',
        'setuptools',
        'numpy',
        'requests'
    ],
    zip_safe=True,
    maintainer='falten ben falten',
    maintainer_email='falten@example.com',
    description='The talker_py package',
    license='BSD',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    entry_points={
        'console_scripts': [
            'amiga_twist_control = twist_control:main',
            'amiga_streams_node = amiga_streams:main',
        ],
    },
)

