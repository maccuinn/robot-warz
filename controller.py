from actor import Actor


class Controller:
    """
    controls an actor
    """

    def __init__(self, actor: Actor):
        """
        :type actor: Actor
        :param actor: the actor to move
        """
        assert isinstance(actor, Actor)
        self.actor = actor
