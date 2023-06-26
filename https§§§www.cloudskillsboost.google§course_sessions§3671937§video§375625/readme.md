# <https§§§www.cloudskillsboost.google§course_sessions§3671937§video§375625>

> [https://www.cloudskillsboost.google/course_sessions/3671937/video/375625](https://www.cloudskillsboost.google/course_sessions/3671937/video/375625)

# Introducing JOINs and UNIONs

![1687722383407.png](./1687722383407.png)

enrich dataset awith union and joins

![1687722416154.png](./1687722416154.png)

2 diff tables and a field, we can join them

![1687722445773.png](./1687722445773.png)

multiple tables with historical data, we can unon them

![1687722515049.png](./1687722515049.png)

weather records

![1687722527359.png](./1687722527359.png)

a lot of tables with readings

![1687722569514.png](./1687722569514.png)

we need uniq id to identify the stations

the regular COUNT and then the COUNT DISTINCT. That's a quick way to see whether or not those records are the same, meaning that it is unique for those roll counts.

![1687722658722.png](./1687722658722.png)

create your uniq uisng a combination

![1687722682323.png](./1687722682323.png)

ex usaf + eban

![1687722737804.png](./1687722737804.png)

![1687722746214.png](./1687722746214.png)

table with same schema can be unioned

distinct union or union all

![1687722795381.png](./1687722795381.png)

# Use table wildcards for easy merges

![1687722824773.png](./1687722824773.png)

it will take for ever

![1687722848005.png](./1687722848005.png)

similar to like op, w can use wildcard on table names

![1687722853838.png](./1687722853838.png)

we can filter

![1687722910841.png](./1687722910841.png)

![1687722940600.png](./1687722940600.png)

pitfalls

![1687722962210.png](./1687722962210.png)

use dataprep if needed to prepare tables before union

![1687723012005.png](./1687723012005.png)

# Linking data across multiple tables

![1687723045156.png](./1687723045156.png)

link multiple tables

horizontally , unuion does somehow vertically

![1687757243626.png](./1687757243626.png)

- use of dot notation
- use of alias
- on clause

match the condition

![1687757318626.png](./1687757318626.png)

let's see what type of joins

![1687757394328.png](./1687757394328.png)

and join details

![1687757424883.png](./1687757424883.png)

# SQL Join examples

![1687757440908.png](./1687757440908.png)

A left is considered an Outer Join. So it's actually Left Outer Join, and Right Outer Join, and Full Outer Join.

![1687757507166.png](./1687757507166.png)

# Avoiding pitfalls when merging datasets

![1687757602626.png](./1687757602626.png)

> be careful of th cartesian product

And the way you can avoid it is the third bullet point here, is knowing the relationship between the tables and your data before you do that JOIN.

![1687757704324.png](./1687757704324.png)

![1687757723057.png](./1687757723057.png)

and 

 ![1687757785229.png](./1687757785229.png)

> imagine on million of rows

how to avoid?

 ![1687757831887.png](./1687757831887.png)

> practice count and cunt distinct first to do joins

 ![1687757877826.png](./1687757877826.png)



The best advice I can give you when starting out is to really understand how your data tables are supposed to be related to each other-- like customers to orders, supplier to inventory-- but being able to back that up by verifying those relationships through SQL. Remember, all data is dirty data. And it's your job to investigate it and interrogate it
before it potentially pollutes your larger dataset with JOINs and UNIONs. And once you understand the relationships between your tables, use UNIONs to append records into a consolidated table and JOINs
to enrich your data with other data sources


# Recap of Google Analytics ecommerce dataset

 ![1687757986752.png](./1687757986752.png)


 ![1687758039817.png](./1687758039817.png)

It has over a million site hits and transaction records
to include insights like what users were close to transacting but never completed, what top keywords are high-value customers using to reach the site, and what top channels are customers going
through to reach your site.



# Troubleshooting and Solving Data Join Pitfalls v1.5

https://www.cloudskillsboost.google/course_sessions/3671937/labs/375631
