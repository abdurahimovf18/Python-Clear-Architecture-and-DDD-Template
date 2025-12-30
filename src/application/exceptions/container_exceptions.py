from src.shared.exceptions import ApplicationException, InternalError


class ContainerException(ApplicationException):
    pass


class InterfaceNotRegisteredError(ContainerException, InternalError):
    """
    Raised on attempt to access unregistered Interface.
    """
    pass


class InterfaceAlreadyRegisteredError(ContainerException, InternalError):
    """
    Raised on attempt to register the realization of the same interface twice.
    """
    pass
