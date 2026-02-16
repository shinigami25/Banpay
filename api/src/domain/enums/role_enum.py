import enum


class RoleEnum(str, enum.Enum):
    ADMIN = "admin"
    FILMS = "films"
    PEOPLE = "people"
    LOCATIONS = "locations"
    SPECIES = "species"
    VEHICLES = "vehicles"
