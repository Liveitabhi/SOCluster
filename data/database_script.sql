USE stackoverflow;

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

LOAD XML LOCAL INFILE '/LOCATION/TO/Posts.xml'
INTO TABLE Posts
ROWS identified BY '<row>';

create index posts_idx_1 on posts(PostTypeId);
