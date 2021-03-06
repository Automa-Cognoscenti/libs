import rospy

from iawake.core.types import ReturnType


class Node(object):
    def __init__(
            self,
            node_name,
            publishing_topic,
            publishing_msg,
    ):
        self._publisher = rospy.Publisher(
            publishing_topic,
            publishing_msg,
            queue_size=10,
        )
        rospy.init_node(node_name)

    @staticmethod
    def _generate_publishable_output(output):
        return [value for _, value in output.items()]

    def publish(self, output):
        if isinstance(output, list):
            return self._publisher.publish(
                self._publisher.data_class(items=output)
            )
        elif isinstance(output, ReturnType):
            return self._publisher.publish(
                *self._generate_publishable_output(output)
            )
        else:
            return self._publisher.publish(output)

    @staticmethod
    def run():
        rospy.spin()
