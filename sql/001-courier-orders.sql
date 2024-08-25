select c."login" as "courier_login",
       count(1)  as "order_qty"
from "Orders" as o
         left join "Couriers" as c on o."courierId" = c."id"
where o."inDelivery" is true
group by c."login";
