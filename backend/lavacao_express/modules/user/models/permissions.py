from sqlmodel import Relationship, SQLModel, Field


class Permission(SQLModel, table=True):
    __tablename__: str = "permission"

    id: int = Field(primary_key=True)
    name: str
    is_active: bool = Field(default=True)
    user_permissions: "UserPermissions" = Relationship(back_populates="permissions")  # type: ignore


class PermissionGroup(SQLModel, table=True):
    __tablename__: str = "permission_group"

    id: int = Field(primary_key=True)
    name: str


# class GroupPermissions(SQLModel, table=True):
#     permission_id: int = Relationship(foreign_key="permission.id")
#     permission_group_id: int = Relationship(foreign_key="permission_group.id")
