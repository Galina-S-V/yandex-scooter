select c."login" as "courier_login",
       count(1)  as "order_qty"
from "Orders" as o
         -- Предполагаем, что заказ не может быть в статусе "в работе",
         -- если с ним не связан курьер. Наличие null-ов в колонке с логинами
         -- будет означать, что что-то пошло не так, и поможет выявить ошибку в данных.
         -- Поэтому здесь left join вместо inner join
         left join "Couriers" as c on o."courierId" = c."id"
where o."inDelivery" is true
group by c."login";
