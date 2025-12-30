from src.shared.exceptions import ApplicationException, InternalError


class EventBusException(ApplicationException):
    pass


class EventBusAlreadyStartedError(EventBusException, InternalError):
    """
    Raised on attempt to call .start method second time without closing.
    """
    pass


class EventBusAlreadyClosedError(EventBusException, InternalError):
    """
    Raised on attempt to call .close method second time without starting.
    """
    pass


class EventBusNotStartedError(EventBusException, InternalError):
    """
    Raised on attempt to use event bus before starting it.
    """
    pass


class EventBusSetupError(EventBusException, InternalError):
    """
    Raised on attempt to use event bus with incorrect setup.
    """
    pass