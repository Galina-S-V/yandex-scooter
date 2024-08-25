select "track",
       case
           when "finished" is true then 2
           when "cancelled" is true then -1
           when "inDelivery" is true then 1
           else 0
           end as "status_code"
from "Orders";
