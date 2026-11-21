-- LernTool online: Tabellen in Supabase anlegen (SQL Editor → New query → einfügen → Run).
-- Zugriff nur über die Vercel-Funktionen mit dem service_role-Schlüssel.
-- RLS ist an und es gibt absichtlich keine Regeln: Mit dem öffentlichen anon-Schlüssel kommt niemand an die Daten.

create table if not exists codes (
  code      text primary key check (code ~ '^[A-Z0-9]{10}$'),
  notiz     text not null default '',
  gesperrt  boolean not null default false,
  erstellt  timestamptz not null default now()
);

create table if not exists geraete (
  code      text not null references codes(code) on delete cascade,
  geraet    text not null,
  name      text not null default '',
  erstellt  timestamptz not null default now(),
  zuletzt   timestamptz not null default now(),
  primary key (code, geraet)
);

create table if not exists lernstand (
  code      text primary key references codes(code) on delete cascade,
  daten     jsonb not null default '{}'::jsonb,
  version   integer not null default 0,
  geaendert timestamptz not null default now()
);

alter table codes     enable row level security;
alter table geraete   enable row level security;
alter table lernstand enable row level security;
