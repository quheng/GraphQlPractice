## aim
use these project to practice GraphQL

## usage
todo

## test sample
1.
```
{
  acquisitions(where:"id=1"){
    priceAmount

    acquiring{
      name
      homepageUrl
    }
    acquired{
      name
      investmentRounds
    }
    createdAt
  }
}
```
2.
```
{
  people(where:"id='1'"){
    firstName
    lastName
    degrees{
      subject
      degreeType
      institution
    }
  }
}
```

3.
```
{
  fundingRounds(where:"funding_round_code = 'angel', raised_amount > 15000000"){
    fundingRoundCode
    raisedAmountUsd
    sourceUrl
    company{
      name
      countryCode
      homepageUrl
    }
  }
}
```
4.
```
{
  funds(where:"raised_amount < 5"){
    name
    sourceUrl
    sourceDescription
  }
}
```
5.
```
{
  ipos(where:"raised_amount > 10000000000"){
    valuationAmount
    publicAt
    stockSymbol
  }
}
```
6.
```
{
  milestones(where:"object_id = 'c:1'"){
    description
    milestoneAt
  }
}
```
7.
```
{
  offices(where:"object_id = 'c:1'"){
    description
    address1
    address2
    zipCode
  }
}
```
8.
```
{
  relationships(where:"person_object_id = 'p:111'"){
    title
    createdAt
  }
}
```
9.
```
{
  people(where:"object_id = 'p:2'"){
    affiliationName
    firstName
    lastName
  }
}
```
## notes
1. In this [https://data.crunchbase.com/docs/2013-snapshot](https://data.crunchbase.com/docs/2013-snapshot) just provide advanced account register. If you want to register a basic account, should go to [https://data.crunchbase.com/page/basic-access-form](https://data.crunchbase.com/page/basic-access-form). Further, better use Gmail to register account. If you use another e-mail, you may lose their reply.
2. I can not visited [http://graphql.org](http://graphql.org), but I get their source code from [here](https://github.com/graphql/graphql.github.io). I read their documents and example from this.
3. In `cb_objects`, all of `parent_id` is null.
4. In `cb_funding_rounds`, some `object_id` can not found at `cb_objects`
