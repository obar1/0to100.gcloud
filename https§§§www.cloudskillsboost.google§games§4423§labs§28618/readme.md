# <https§§§www.cloudskillsboost.google§games§4423§labs§28618>
> <https://www.cloudskillsboost.google/games/4423/labs/28618>

# Troubleshooting Data Models in Looker

## Tools for troubleshooting LookML code and common use cases

[https://docs.looker.com/data-modeling/getting-started/lookml-validation#validating_your_lookml](../https§§§docs.looker.com§data-modeling§getting-started§lookml-validation#validating_your_lookml/readme.md)
SQL Runner
Content Validator
[https://docs.looker.com/reference/looker-error-catalog](../https§§§docs.looker.com§reference§looker-error-catalog/readme.md)

## Task 1. Use SQL Runner to explore available data and troubleshoot SQL queries

![Alt text](image-2.png)

![Alt text](image-3.png)

![Alt text](image-4.png)

issue

![Alt text](image-5.png)

works now

![Alt text](image-6.png)

add to project
![Alt text](image-7.png)

saved as  view
![Alt tex](image-8.png)

modify model

![Alt text](image-9.png)

push 
![Alt text](image-10.png)

available in sql runner
![Alt text](image-11.png)

## Task 2. Use the LookML Validator to test syntax and validate relationships defined in the model

syntax error

![Alt text](image-12.png)

![Alt text](image-13.png)

```
dimension: average_sales  {
   type: number
   sql: ${user_order_lifetime.lifetime_sales} /
     ${user_order_lifetime.lifetime_orders} ;;
   value_format_name: usd
  }```

![](image-14.png)

[https://docs.looker.com/reference/looker-error-catalog](../https§§§docs.looker.com§reference§looker-error-catalog/readme.md)

