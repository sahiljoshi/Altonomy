steps: 

`docker-compose  build  grafana
docker-compose up -d grafana
`

run grafana in browser : 

`localhost:3000`
`username : admin` 
`password : admin`

Add mysql data source with following credentials:

`host: test_mysql_db`
`port 3006`


create a  dashboard/panel

using following  query 


_`SELECT
  last_update_time as time_sec,
  (bid+ask)/2 as value,
  bid as value2 ,
  concat (symbol  , exchange) as metric
FROM bid_ask_data
WHERE last_update_time
ORDER BY last_update_time ASC`_


and use time series option. 

This will show chart in the panel  

