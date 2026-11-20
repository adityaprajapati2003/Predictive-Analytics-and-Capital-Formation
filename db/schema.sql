CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE founders (id SERIAL PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL);
CREATE TABLE startups (
  id SERIAL PRIMARY KEY, founder_id INT REFERENCES founders(id),
  name TEXT NOT NULL, subsector TEXT, stage TEXT, geography TEXT);
CREATE TABLE pitch_decks (
  id SERIAL PRIMARY KEY, startup_id INT REFERENCES startups(id),
  file_path TEXT, extracted_text TEXT, embedding vector(384), uploaded_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE investors (
  id SERIAL PRIMARY KEY, name TEXT NOT NULL, investor_type TEXT, thesis TEXT,
  stage_pref TEXT, check_min NUMERIC, check_max NUMERIC, embedding vector(384));
CREATE TABLE fundability_scores (
  id SERIAL PRIMARY KEY, startup_id INT REFERENCES startups(id),
  probability DOUBLE PRECISION, model_version TEXT, explanation JSONB, computed_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE matches (
  id SERIAL PRIMARY KEY, startup_id INT REFERENCES startups(id), investor_id INT REFERENCES investors(id),
  compatibility DOUBLE PRECISION, status TEXT DEFAULT 'suggested');
CREATE TABLE market_snapshots (id SERIAL PRIMARY KEY, snapshot_date DATE, indicators JSONB);
CREATE TABLE funding_rounds (
  id SERIAL PRIMARY KEY, startup_id INT REFERENCES startups(id),
  round_type TEXT, amount NUMERIC, announced_on DATE);
CREATE TABLE consent_records (
  id SERIAL PRIMARY KEY, user_id INT, purpose TEXT, granted BOOLEAN, recorded_at TIMESTAMPTZ DEFAULT now());
