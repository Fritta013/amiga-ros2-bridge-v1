from setuptools import setup

package_name = 'amiga-ros-bridge'


setup(
    name=package_name,
    version='1.0.0',
    install_requires=['setuptools'],
    packages=[src],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
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
        'amiga_twist_control = src.twist_control:main',
        'amiga_streams_node = src.amiga_streams:main',

    ],
},



)
