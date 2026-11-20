"""SQLAlchemy tables. Mirrors db/schema.sql and the ER diagram."""
from datetime import date, datetime

from sqlalchemy import JSON, Boolean, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Founder(Base):
    __tablename__ = "founders"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    startups: Mapped[list["Startup"]] = relationship(back_populates="founder")


class Startup(Base):
    __tablename__ = "startups"
    id: Mapped[int] = mapped_column(primary_key=True)
    founder_id: Mapped[int] = mapped_column(ForeignKey("founders.id"))
    name: Mapped[str] = mapped_column(String(200))
    subsector: Mapped[str] = mapped_column(String(100))
    stage: Mapped[str] = mapped_column(String(50))
    geography: Mapped[str | None] = mapped_column(String(100))
    founder: Mapped[Founder] = relationship(back_populates="startups")


class PitchDeck(Base):
    __tablename__ = "pitch_decks"
    id: Mapped[int] = mapped_column(primary_key=True)
    startup_id: Mapped[int] = mapped_column(ForeignKey("startups.id"))
    file_path: Mapped[str] = mapped_column(String(500))
    extracted_text: Mapped[str | None]
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Investor(Base):
    __tablename__ = "investors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    investor_type: Mapped[str] = mapped_column(String(50))
    thesis: Mapped[str | None]
    stage_pref: Mapped[str | None] = mapped_column(String(100))
    check_min: Mapped[float | None] = mapped_column(Float)
    check_max: Mapped[float | None] = mapped_column(Float)


class FundabilityScore(Base):
    __tablename__ = "fundability_scores"
    id: Mapped[int] = mapped_column(primary_key=True)
    startup_id: Mapped[int] = mapped_column(ForeignKey("startups.id"))
    probability: Mapped[float] = mapped_column(Float)
    model_version: Mapped[str] = mapped_column(String(50))
    explanation: Mapped[dict] = mapped_column(JSON, default=dict)
    computed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Match(Base):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True)
    startup_id: Mapped[int] = mapped_column(ForeignKey("startups.id"))
    investor_id: Mapped[int] = mapped_column(ForeignKey("investors.id"))
    compatibility: Mapped[float] = mapped_column(Float)  # a ranking score, not a probability
    status: Mapped[str] = mapped_column(String(30), default="suggested")


class MarketSnapshot(Base):
    __tablename__ = "market_snapshots"
    id: Mapped[int] = mapped_column(primary_key=True)
    snapshot_date: Mapped[date] = mapped_column(Date)
    indicators: Mapped[dict] = mapped_column(JSON, default=dict)


class FundingRound(Base):
    __tablename__ = "funding_rounds"
    id: Mapped[int] = mapped_column(primary_key=True)
    startup_id: Mapped[int] = mapped_column(ForeignKey("startups.id"))
    round_type: Mapped[str] = mapped_column(String(50))
    amount: Mapped[float | None] = mapped_column(Float)
    announced_on: Mapped[date | None] = mapped_column(Date)


class ConsentRecordRow(Base):
    __tablename__ = "consent_records"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    purpose: Mapped[str] = mapped_column(String(50))
    granted: Mapped[bool] = mapped_column(Boolean)
    recorded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
