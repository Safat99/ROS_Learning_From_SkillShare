from setuptools import setup
import os
from glob import glob

package_name = 'my_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        ## all the additional files in the launch/* folder packages are copied into this share folder,package_name,launch file
        ## if we open the home folder(ws) then install/my_python_pkg/share, we can find all the files there
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='safat',
    maintainer_email='sarkersafat99@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = my_python_pkg.my_first_node:main",
            "robot_news_station = my_python_pkg.robot_news_station:main",
            "smartphone = my_python_pkg.smartphone:main",
            "number_publisher = my_python_pkg.number_publisher:main",
            "number_counter = my_python_pkg.number_counter:main",
            "add_two_ints_server = my_python_pkg.add_two_ints_server:main"
        ],
    },
)
