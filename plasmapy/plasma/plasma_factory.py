from plasmapy.plasma.plasma_base import GenericPlasma
from plasmapy.utils.datatype_factory_base import (
    BasicRegistrationFactory,
    MultipleMatchError,
    NoMatchError,
    ValidationFunctionError,
)

__all__ = ["PlasmaFactory", "Plasma"]


class PlasmaFactory(BasicRegistrationFactory):
    """
    Plasma factory class. Used to create a variety of Plasma objects.
    Valid plasma structures are specified by registering them with the
    factory.
    """

    pass


Plasma = PlasmaFactory(
    default_widget_type=GenericPlasma,
    registry=GenericPlasma._registry,
    additional_validation_functions=["is_datasource_for"],
)
