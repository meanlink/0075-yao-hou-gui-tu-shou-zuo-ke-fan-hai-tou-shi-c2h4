CREATE TABLE IF NOT EXISTS studios(
 code text PRIMARY KEY,name text NOT NULL
);
CREATE TABLE IF NOT EXISTS workshops(
 code text PRIMARY KEY,title text NOT NULL,home text NOT NULL REFERENCES studios(code),
 end_date date NOT NULL, pickup_through date NOT NULL CHECK(pickup_through>=end_date)
);
CREATE TABLE IF NOT EXISTS ceramics(
 tag text PRIMARY KEY,workshop text NOT NULL REFERENCES workshops(code),title text NOT NULL,
 claim_code text NOT NULL, status text NOT NULL DEFAULT 'ready' CHECK(status IN ('ready','moving','collected')),
 site text NOT NULL REFERENCES studios(code), UNIQUE(workshop,claim_code)
);
CREATE TABLE IF NOT EXISTS carrier_slips(
 id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,tag text NOT NULL REFERENCES ceramics(tag),
 origin text NOT NULL REFERENCES studios(code), destination text NOT NULL REFERENCES studios(code),
 state text NOT NULL DEFAULT 'out' CHECK(state IN ('out','accepted','returned')),
 handler text NOT NULL REFERENCES app_users(email), accepted_by text REFERENCES app_users(email),
 CHECK(origin<>destination),CHECK((state='out')=(accepted_by IS NULL))
);
CREATE UNIQUE INDEX IF NOT EXISTS active_carriage ON carrier_slips(tag) WHERE state='out';
CREATE TABLE IF NOT EXISTS claim_checks(
 tag text PRIMARY KEY REFERENCES ceramics(tag), studio text NOT NULL REFERENCES studios(code),
 local_day date NOT NULL, receiver text NOT NULL, checked_by text NOT NULL REFERENCES app_users(email)
);
CREATE TABLE IF NOT EXISTS return_snapshots(
 workshop text PRIMARY KEY REFERENCES workshops(code), reviewer text NOT NULL REFERENCES app_users(email),
 detail jsonb NOT NULL, job bigint UNIQUE NOT NULL REFERENCES app_jobs(id)
);
