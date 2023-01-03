# wd_gov_refs

This script adds GOV ids to the P2503 property of Wikidata items representing geographical/administrative entities in Poland, mainly settlements.

The Wikidata-GOV references were derived beforehand by combining references present in various trustworthy datasets (TERYT/SIMC, GND, GOV, ...) which were stored in a PostgreSQL table ("refs_wd_gov").

After the creation of the data set, additional automated plausibility checks between all linked Wikidata and GOV datasets were performed, using the PostgreSQL Levenshtein function (name similarity) and PostGIS capabilities (geographical proximity), backing the reference claims (high name similarity and geographical proximity of the pairs).

This data is written into the P2503 property of the respective Wikidata item. If a Wikidata item already contains a GOV reference, it is left unchanged.
