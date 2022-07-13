# Following SkillShare ROS2 course of total 90 videos 

### Introduction 
	ROS is something between middleware and a framework but especially for robot applications
### Goals
	> can be used on any robots
	> you don’t need to reinvent the wheel
### Advantage 
	* code separation
	* plug and play libraries >> navigation 
	* libraries >> we can use both languages on the same project

Installation
	Documentation ( vdo 4-8)
	Demo node >> vdo 9 ( ros node talker receiver) 

```source /opt/ros/foxy/setup.bash```


### VDO 10 >>>
	ros2 run demo_nodes_cpp talker
	ros2 run demo_nodes_cpp listener
Learning 
	>> LTS >> long term support, terminator for multi terminal

### VDO 11 >> 
	to setup new node .., create package , rewrite the node inside the package, save compile run >>>

## VDO 12 >>> 
	colcon build, colcon-extension package install 
	colcon to create my own ros2 program we need a build tool specialized for ros2 which is named colcon..
```sudo apt install python3-colcon-common-extensions```
We also need to enable also autocompletion features of colcon which has to run everytime
```cd usr/share/colcon_argcomplete/hook/```
```source colcon-argcomplete.bash```
—----------------------------------------------------------------------------------------------------------
Learning >>> if we wanna start something source every time, we can add that to the ~/.bashrc file  >> that means it will run every time after a terminal is opened…
—----------------------------------------------------------------------------------------------------------
Vdo 13 >>> mkdir ros_learning, cd ros…, 
mkdir ros2_ws(workspace), cd workspace, mkdir src
 colcon build (for building the workspace)
Add the install/setup.bash to the ./bashrc folder
Source the install file
Vdo 14 
To create a ros2 node we need to create a package
>> Package create >>   cd src >> 
``` ros2 pkg create my_py_pkg –build-type ament_python  –dependencies rclpy```
Dependency  r jonne –dependency rclpy``` >> ros python library lagbe
 Build type >> cpp  er jonne ekdhorener aar python er jonne ament_python
``` cd my_py_pkg```
Package.xml file e gele shob jinish gula details dekha jaabe

Now if we want to compile our package…open a new terminal, go to ros workspace and then type >>
 ``` colcon build```>> build all package
``` colcon build –packages-select my_py_pkg``` >> compile 1 package

That means our python package is now ready to host any python node

VDO 15 >>> ros2 create cpp package
VDO 16 >> > NODES
Nodes communicate to each other on the same package…
Suppose a robot workspace have several packages like camera package, motion planning package, hardware control etc… inside camera package we have camera driver, image processing node etc … nodes are files(codes) inside those packages


Definition >> nodes 
Subprograms in your application, responsible for one thing
Similar to OOP class
Combined into a graph
Communicate with each other through topics,services and parameters
Benefits of nodes >> 
Reduce code complexity
Fault tolerance ( if one node crashes others will not crashed)
One node can be written in python and another c++ can easily communicate
VDO 17 >>> nodes more
—--------------------------------
In this video hands on code on how to create and execute your first ros2 node has demonstrated. So this is an important video
We can execute a node with python3 directly.. Or also we can install it for further functionalitiues.
To install a ros node we have to edit the setup.py file 
But the professional way is different. We will use ```ros2 run package_name executable_file``` >>> ``` ros2 run my_python_pkg py_node``` , here in the setup.py file we named the executable file as py_node


We have to source the local_setup.bash inside the ros2_ws/install folder
We have to include this command to our ~/.bashrc so that we can always get the latest file after opening a terminal

—--------------- summary of episode 17—-----------
We created a python file inside the package folder. Inside that python file we created a node using Node class with the constructor for node name..and then run and install our python node

---------------------------------------------------------------------------------------------------------------------

### VDO 18 
#### nodes with oop
* For making our program more scalable we should use OOP in writing the code of the node
Changed the nodes code for oop
Compiile the node again from the workspace directory using 

```colon build —packages-select my_python_pkg```

To see more check my_first_node.py code

----------------------------------------------------------------------------------------------------------------------------
Vdo 19 >> nodes with cpp >>> skipping this right now

