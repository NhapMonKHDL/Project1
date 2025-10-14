--5, Lấy Doanh thu theo quốc gia (Customer.Country), giảm dần; chỉ hiển thị quốc gia có doanh thu > 1000 
select * from invoice;

select * from customer;

with country_invoiceid as (
    select country, invoiceid
    from customer join invoice using (customerid)
)
select country , total_profit
from (
    select country ,sum(total) over(partition by country) total_profit
    from (select country, total from country_invoiceid join invoice using (invoiceid)) c_i
    )
where total_profit > 1000 order by total_profit DESC;


-- 8, Tìm ra khách hàng có tổng chi tiêu cao nhất (tổng Invoice.Total theo CustomerId). 
with cus_invoice as (
    select customerid,firstname, lastname, invoiceid , total
    from customer join invoice using (customerid)
)
select distinct *
from (
    select customerid, sum(total) over(partition by customerid) total_purchase from cus_invoice
    )
order by total_purchase;

    