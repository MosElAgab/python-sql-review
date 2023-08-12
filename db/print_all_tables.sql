\c nc_sells_fridges_draft

\echo '\ntables:\n'
\dt
\echo '\n- items\n'
SELECT * FROM items;
\echo '\n- sales\n'
SELECT * FROM sales;
\echo '\n- staff\n'
SELECT * FROM staff;


\c nc_sells_fridges

\echo '\nnew tables:\n'
\dt
\echo '\n- dim_department\n'
SELECT * FROM dim_department;

\echo '\n- dim_features\n'
SELECT * FROM dim_features;

\echo '\n- dim_stock\n'
SELECT * FROM dim_stock;

\echo '\n- stock_feature_junc\n'
SELECT * FROM stock_feature_junc;

\echo '\n- dim_staff\n'
SELECT * FROM dim_staff;

\echo '\n- fact_sales\n'
SELECT * FROM fact_sales;