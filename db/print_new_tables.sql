\c nc_sells_fridges

\echo '\nnew tables:\n'
\dt
\echo '\n- dim_department\n'
SELECT * FROM dim_department;

\echo '\n- dim_features\n'
SELECT * FROM dim_features;

\echo '\n- dim_stock\n'
SELECT * FROM dim_stock;
