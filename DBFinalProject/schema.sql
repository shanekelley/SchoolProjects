drop table if exists AccountInfo;
create table AccountInfo (
  AccNum integer primary key,
  username text,
  password text,
  email text
);

drop table if exists AccountBal;
create table AccountBal (
  AccNum integer primary key,
  bitcoinBal float,
  moneroBal float,
  ethereumBal float,
  totalBal float
);

drop table if exists CoinData;
create table CoinData (
  symbol text primary key,
  name text,
  tradeVolume integer,
  price float
);

drop table if exists CoinChanges;
create table CoinChanges (
  symbol text primary key,
  oneday float,
  oneweek float,
  onemonth float,
  threemonths float,
  oneyear float
);

drop table if exists Transactions;
create table Transactions (
  transactionNum integer primary key,
  DepositWithdrawal text,
  AccNum integer,
  amount float,
  coinSymbol text,
  transactionFee float,
  date datetime
);

drop table if exists Fee;
create table Fee (
  transactionNum integer primary key,
  transactionFee float,
  coinSymbol text,
  updatedCompBal float,
  date datetime
);

drop table if exists MethodOfPayment;
create table MethodOfPayment (
  AccNum integer,
  methodOfPayment text,
  AuthorizationAmount float,
  coinSymbol text
);

drop table if exists CreditDebit;
create table CreditDebit (
  AccNum integer,
  nameOnCard text,
  cardNum integer,
  CVC integer,
  expirationDate text
);

drop table if exists Paypal;
create table paypal (
  AccNum integer,
  PaypalAccNum integer,
  nameOnAcc text
);

drop table if exists TotalMarketInfo;
create table  TotalMarketInfo(
  coinSymbol text primary key,
  marketCap integer,
  TwentyFourHourVol integer,
  marketSupply integer
);

drop table if exists AccInfoHasMP;
create table AccInfoHasMP (
  AccNum integer primary key
);

drop table if exists Relies;
create table Relies (
  AccNum integer primary key,
  coinSymbol text
);

drop table if exists CoinDataHasCoinChanges;
create table CoinDataHasCoinChanges (
  coinSymbol text
);

drop table if exists AccbalHasTrans;
create table AccbalHasTrans (
  AccNum integer primary key,
  transactionNum integer
);

drop table if exists Affects;
create table Affects (
  coinSymbol text
);
 