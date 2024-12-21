import time
from typing import List

from sqlalchemy import (
    Integer,
    BigInteger,
    Text,
    Boolean,
    UniqueConstraint,
    ARRAY,
)
from sqlalchemy.orm import declarative_base, mapped_column, Mapped



from utils.CONSTANTS import LEVELS_AND_XP
from utils.shortcuts import get_expiry

Base = declarative_base()


class Tag(Base):
    __tablename__ = "tags"
    name:Mapped[str] = mapped_column(Text, primary_key=True)
    content:Mapped[str] = mapped_column(Text)
    owner:Mapped[int] = mapped_column(BigInteger)
    created_at:Mapped[int]  = mapped_column(BigInteger)
    views:Mapped[int] = mapped_column(Integer)


class TagRelations(Base):
    __tablename__ = "tag_relations"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(Text)
    alias:Mapped[str] = mapped_column(Text)


class Blacklist(Base):
    __tablename__ = "blacklist"
    id:Mapped[int]  = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int]  = mapped_column(BigInteger)
    reason:Mapped[str] = mapped_column(Text)
    bot:Mapped[bool] = mapped_column(Boolean)
    tickets:Mapped[bool] = mapped_column(Boolean)
    tags:Mapped[bool] = mapped_column(Boolean)
    expires:Mapped[int] = mapped_column(BigInteger)

    def is_expired(self):
        if self.expires == 9999999999:
            return False
        return int(time.time()) > self.expires

    @property
    def get_expiry(self):
        return get_expiry(self.expires)


class FlagQuiz(Base):
    __tablename__ = "flag_quiz"
    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger)
    tries:Mapped[int] = mapped_column(Integer)
    correct:Mapped[int] = mapped_column(Integer)
    completed:Mapped[int] = mapped_column(Integer)
    guild_id:Mapped[int] = mapped_column(BigInteger)


class Trivia(Base):
    __tablename__ = "trivia"
    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger)
    correct:Mapped[int] = mapped_column(Integer)
    incorrect:Mapped[int] = mapped_column(Integer)
    streak:Mapped[int] = mapped_column(Integer)
    longest_streak:Mapped[int] = mapped_column(Integer)


class ReactionRole(Base):
    __tablename__ = "reaction_roles"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    message_id:Mapped[int] = mapped_column(BigInteger)
    role_id:Mapped[int] = mapped_column(BigInteger)
    emoji:Mapped[str] = mapped_column(Text)
    roles_given:Mapped[int] = mapped_column(Integer, default=0)


class Warnings(Base):
    __tablename__ = "warnings"
    warning_id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger)
    moderator_id:Mapped[int] = mapped_column(BigInteger)
    reason:Mapped[str] = mapped_column(Text)
    guild_id:Mapped[int] = mapped_column(BigInteger)


class Levels(Base):
    __tablename__ = "levels"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger)
    user_id:Mapped[int] = mapped_column(BigInteger)
    total_xp:Mapped[int] = mapped_column(Integer, default=0)

    @property
    def level(self):
        # get users level based on total xp
        for level, xp in LEVELS_AND_XP.items():
            if self.total_xp < xp:
                return level - 1

    @property
    def xp(self):
        # get users xp based on total xp
        for level, xp in LEVELS_AND_XP.items():
            if self.total_xp < xp:
                return self.total_xp - LEVELS_AND_XP[level - 1]


class CustomRoles(Base):
    __tablename__ = "custom_roles"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger)
    role_id:Mapped[int] = mapped_column(BigInteger)
    user_id:Mapped[int] = mapped_column(BigInteger)


class RoleReward(Base):
    __tablename__ = "role_rewards"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger)
    role_id:Mapped[int] = mapped_column(BigInteger)
    required_lvl:Mapped[int] = mapped_column(Integer, default=0)


class Birthday(Base):
    __tablename__ = "birthday"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger)
    birthday:Mapped[str] = mapped_column(Text, default=None)
    birthday_last_changed:Mapped[int] = mapped_column(BigInteger, default=None)


class Timezone(Base):
    __tablename__ = "timezone"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(BigInteger)
    timezone:Mapped[str] = mapped_column(Text, default=None)
    timezone_last_changed:Mapped[int] = mapped_column(BigInteger, default=None)


class Config(Base):
    __tablename__ = "config"
    guild_id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    xp_boost:Mapped[int] = mapped_column(Integer, default=1)
    xp_boost_expiry:Mapped[int] = mapped_column(BigInteger, default=0)
    xp_boost_enabled:Mapped[bool] = mapped_column(Boolean, default=True)
    custom_roles_threshold:Mapped[int] = mapped_column(Integer, default=20)
    min_required_lvl:Mapped[int] = mapped_column(Integer, default=5)
    position_role_id:Mapped[int] = mapped_column(BigInteger, default=None)

    @property
    def boost_expired(self) -> bool:
        now = int(time.time())
        if self.xp_boost_expiry >= now:
            return False
        return True

    @property
    def boost_time_left(self) -> int:
        now = int(time.time())
        return self.xp_boost_expiry - now

    @property
    def get_boost(self) -> int:
        return self.xp_boost

    @property
    def xp_boost_active(self) -> bool:
        return bool(self.xp_boost_enabled) and not self.boost_expired


class Commands(Base):
    __tablename__: str = "commands"
    __table_args__: tuple[UniqueConstraint] = (UniqueConstraint("guild_id", "command"),)
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger)
    command:Mapped[str] = mapped_column(Text)
    command_used:Mapped[int] = mapped_column(Integer, default=0)


class TotalCommands(Base):
    __tablename__ = "total_commands"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger, unique=True)
    total_commands_used:Mapped[int] = mapped_column(Integer, default=0)


class AutoResponseMessages(Base):
    __tablename__ = "auto_response_messages"
    # needs to be list of strings and list of regex strings, channels, guild and response
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    guild_id:Mapped[int] = mapped_column(BigInteger)
    channel_ids:Mapped[List[int]] = mapped_column(ARRAY(BigInteger))
    regex_strings:Mapped[List[str]] = mapped_column(ARRAY(Text))
    strings :Mapped[List[str]]= mapped_column(ARRAY(Text))
    response:Mapped[str] = mapped_column(Text)
    case_sensitive:Mapped[bool] = mapped_column(Boolean, default=False)
    enabled :Mapped[bool]= mapped_column(Boolean, default=True)
