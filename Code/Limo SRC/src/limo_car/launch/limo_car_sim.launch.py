from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    pkg_share = FindPackageShare('limo_car')

    world_file = PathJoinSubstitution([pkg_share, 'worlds', 'empty.world'])
    xacro_file = PathJoinSubstitution([pkg_share, 'urdf', 'limo_car.urdf.xacro'])

    robot_description = ParameterValue(
    Command(['xacro ', xacro_file]),
    value_type=str
    
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])
        ),
        launch_arguments={
            'world': world_file,
            'use_sim_time': 'True' 
            }.items()
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description,'use_sim_time': True}]
    )

    robot_desc_pub = Node(
        package='limo_car',
        executable='robot_description_publisher.py',
        output='screen',
        parameters=[{'xacro_file': xacro_file}]
    )

    spawner = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'limo_car',
            '-x', '0', '-y', '0', '-z', '0.15'
        ]
    )

    # Delay spawn slightly so Gazebo and the description publisher are ready
    delayed_spawn = TimerAction(period=2.0, actions=[spawner])

    return LaunchDescription([
        gazebo_launch,
        rsp,
        robot_desc_pub,
        delayed_spawn
    ])
