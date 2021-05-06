USE stackoverflow;

CREATE TABLE IF NOT EXISTS Badges (
	Id INT NOT NULL PRIMARY KEY,
	UserId INT NOT NULL,
	Name VARCHAR(50) NOT NULL,
	Date DATETIME NOT NULL,
	Class TINYINT NOT NULL,
	TagBased BIT NOT NULL
);

CREATE TABLE IF NOT EXISTS Comments (
    Id INT NOT NULL PRIMARY KEY,
    PostId INT NOT NULL,
    Score INT NOT NULL DEFAULT 0,
    Text VARCHAR(600),
    CreationDate DATETIME NOT NULL,
    UserDisplayName VARCHAR(40),
    UserId INT,
    ContentLicense VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS PostHistory (
    Id INT NOT NULL PRIMARY KEY,
    PostHistoryTypeId TINYINT NOT NULL,
    PostId INT NOT NULL,
    RevisionGUID VARCHAR(36) NOT NULL,
    CreationDate DATETIME NOT NULL,
    UserId INT,
    UserDisplayName VARCHAR(40),
    Comment VARCHAR(400),
    Text TEXT,
    ContentLicense VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS PostLinks (
	Id INT NOT NULL PRIMARY KEY,
  	CreationDate DATETIME NOT NULL,
  	PostId INT NOT NULL,
  	RelatedPostId INT NOT NULL,
  	LinkTypeId TINYINT NOT NULL
);

CREATE TABLE IF NOT EXISTS Posts (
    Id INT NOT NULL PRIMARY KEY,
    PostTypeId TINYINT NOT NULL,
    AcceptedAnswerId INT,
    ParentId INT,
    CreationDate DATETIME NOT NULL,
    DeletionDate DATETIME,
    Score INT NOT NULL,
    ViewCount INT,
    Body TEXT,
    OwnerUserId INT,
    OwnerDisplayName VARCHAR(40),
    LastEditorUserId INT,
    LastEditorDisplayName VARCHAR(40),
    LastEditDate DATETIME,
    LastActivityDate DATETIME,
    Title VARCHAR(250),
    Tags VARCHAR(250),
    AnswerCount INT,
    CommentCount INT,
    FavoriteCount INT,
    ClosedDate DATETIME,
    CommunityOwnedDate DATETIME,
    ContentLicense VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tags (
  	Id INT NOT NULL PRIMARY KEY,
  	TagName VARCHAR(35),
  	Count INT NOT NULL,
  	ExcerptPostId INT,
  	WikiPostId INT
);

CREATE TABLE IF NOT EXISTS Users (
    Id INT NOT NULL PRIMARY KEY,
    Reputation INT NOT NULL,
    CreationDate DATETIME NOT NULL,
    DisplayName VARCHAR(40),
    LastAccessDate  DATETIME NOT NULL,
	WebsiteUrl VARCHAR(200),
	Location VARCHAR(100),
    AboutMe TEXT,
	Views INT NOT NULL,
	UpVotes INT NOT NULL,
    DownVotes INT NOT NULL,
    ProfileImageUrl VARCHAR(200),
	EmailHash VARCHAR(32),
	AccountId INT
);

CREATE TABLE IF NOT EXISTS Votes (
    Id INT NOT NULL PRIMARY KEY,
    PostId INT NOT NULL,
    VoteTypeId TINYINT NOT NULL,
	UserId INT,
    CreationDate DATETIME,
	BountyAmount INT
);

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Badges/Badges_test.xml'
INTO TABLE Badges
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-stackoverflow.com-Comments/Comments_test.xml'
INTO TABLE Comments
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-PostHistory/PostHistory_test.xml'
INTO TABLE PostHistory
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-PostLinks/PostLinks_test.xml'
INTO TABLE PostLinks
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Posts/Posts_test.xml'
INTO TABLE Posts
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Tags/Tags_test.xml'
INTO TABLE Posts
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Users/Users_test.xml'
INTO TABLE Users
ROWS identified BY '<row>';

LOAD XML LOCAL INFILE '/home/nvidia/Desktop/Stackoverflow_Data_Archive/stackoverflow.com-Votes/Votes_test.xml'
INTO TABLE Votes
ROWS identified BY '<row>';

create index badges_idx_1 on badges(UserId);

create index comments_idx_1 on comments(PostId);
create index comments_idx_2 on comments(UserId);

create index post_history_idx_1 on post_history(PostId);
create index post_history_idx_2 on post_history(UserId);

create index posts_idx_1 on posts(AcceptedAnswerId);
create index posts_idx_2 on posts(ParentId);
create index posts_idx_3 on posts(OwnerUserId);
create index posts_idx_4 on posts(LastEditorUserId);

create index votes_idx_1 on votes(PostId);