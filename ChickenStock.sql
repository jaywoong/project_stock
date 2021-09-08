DROP TABLE user;

CREATE TABLE user (
	user_id	int	NOT NULL,
	member_password	char(255)	NOT NULL,
	member_email	varchar(128)	NOT NULL,
	member_name	varchar(128)	NOT NULL
);

DROP TABLE likes;

CREATE TABLE likes (
	likes_id	int	NOT NULL,
	user_id	int	NOT NULL,
	likes_age	int	NOT NULL,
	likes_yearafter	int	NOT NULL,
	likes_amount	int	NOT NULL,
	likes_matters	varchar(128)	NOT NULL,
	likes_lossaction	varchar(128)	NOT NULL
);

DROP TABLE type;

CREATE TABLE type (
	type_id	int	NOT NULL,
	likes_id	int	NOT NULL,
	user_id	int	NOT NULL,
	type_name	varchar(128)	NOT NULL,
	type_risklevel	int	NOT NULL
);

DROP TABLE stock;

CREATE TABLE stock (
	stock_id	int	NOT NULL,
	company_id	int	NOT NULL,
	stock_name	varchar(128)	NOT NULL,
	stock_type	varchar(128)	NOT NULL,
	stock_pastyield	int	NOT NULL,
	stock_futureyield	int	NOT NULL,
	stock_futureprice	int	NOT NULL,
	stock_netsell	int	NOT NULL,
	stock_netbuy	int	NOT NULL,
	stock_closingprice	int	NOT NULL,
	stock_highprice	int	NOT NULL,
	stock_lowprice	int	NOT NULL,
	stock_per	int	NOT NULL,
	stock_pbr	int	NOT NULL
);

DROP TABLE portfolio;

CREATE TABLE portfolio (
	portfolio_id	int	NOT NULL,
	type_id	int	NOT NULL,
	likes_id	int	NOT NULL,
	user_id	int	NOT NULL,
	stock_id	int	NOT NULL,
	company_id	int	NOT NULL,
	portfolio_ratio	int	NOT NULL,
	portfolio_amout	int	NOT NULL,
	portfolio_futureyield	int	NOT NULL,
	portfolio_risk	int	NOT NULL,
	Field	VARCHAR(255)	NULL
);

DROP TABLE company;

CREATE TABLE company (
	company_id	int	NOT NULL,
	company_name	varchar(128)	NOT NULL,
	company_gas	int	NOT NULL,
	company_energy	int	NOT NULL,
	company_dust	int	NOT NULL,
	company_donation	int	NOT NULL,
	company_employeerate	int	NOT NULL,
	company_boardrate	int	NOT NULL,
	company_wagerate	int	NOT NULL
);

ALTER TABLE user ADD CONSTRAINT PK_USER PRIMARY KEY (
	user_id
);

ALTER TABLE likes ADD CONSTRAINT PK_LIKES PRIMARY KEY (
	likes_id,
	user_id
);

ALTER TABLE type ADD CONSTRAINT PK_TYPE PRIMARY KEY (
	type_id,
	likes_id,
	user_id
);

ALTER TABLE stock ADD CONSTRAINT PK_STOCK PRIMARY KEY (
	stock_id,
	company_id
);

ALTER TABLE portfolio ADD CONSTRAINT PK_PORTFOLIO PRIMARY KEY (
	portfolio_id,
	type_id,
	likes_id,
	user_id,
	stock_id,
	company_id
);

ALTER TABLE company ADD CONSTRAINT PK_COMPANY PRIMARY KEY (
	company_id
);

ALTER TABLE likes ADD CONSTRAINT FK_user_TO_likes_1 FOREIGN KEY (
	user_id
)
REFERENCES user (
	user_id
);

ALTER TABLE type ADD CONSTRAINT FK_likes_TO_type_1 FOREIGN KEY (
	likes_id
)
REFERENCES likes (
	likes_id
);

ALTER TABLE type ADD CONSTRAINT FK_likes_TO_type_2 FOREIGN KEY (
	user_id
)
REFERENCES likes (
	user_id
);

ALTER TABLE stock ADD CONSTRAINT FK_company_TO_stock_1 FOREIGN KEY (
	company_id
)
REFERENCES company (
	company_id
);

ALTER TABLE portfolio ADD CONSTRAINT FK_type_TO_portfolio_1 FOREIGN KEY (
	type_id
)
REFERENCES type (
	type_id
);

ALTER TABLE portfolio ADD CONSTRAINT FK_type_TO_portfolio_2 FOREIGN KEY (
	likes_id
)
REFERENCES type (
	likes_id
);

ALTER TABLE portfolio ADD CONSTRAINT FK_type_TO_portfolio_3 FOREIGN KEY (
	user_id
)
REFERENCES type (
	user_id
);

ALTER TABLE portfolio ADD CONSTRAINT FK_stock_TO_portfolio_1 FOREIGN KEY (
	stock_id
)
REFERENCES stock (
	stock_id
);

ALTER TABLE portfolio ADD CONSTRAINT FK_stock_TO_portfolio_2 FOREIGN KEY (
	company_id
)
REFERENCES stock (
	company_id
);

