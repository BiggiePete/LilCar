from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lilcar_states',
            namespace='lilcar_states_pub',
            executable='pub',
            name='lilcar'
        ),
        Node(
            package='lilcar_states',
            namespace='lilcar_states_sub',
            executable='sub',
            name='lilcar'
        )
    ])