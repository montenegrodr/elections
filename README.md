# elections


## Requirements

- Redis 4.0
- MySQL 5.5
- Python 3.6
- ElasticSearch 6.*
- nodejs 8.*

## Database CHARSET and COLLATION

```bash
CREATE DATABASE `elections` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ 
```

sudo apt-get install libmysqlclient-dev python-dev

## ElasticSearch schema

```
PUT news 
{
  "mappings": {
    "doc": { 
      "properties":{ 
        "title":      { "type": "text"  }, 
        "body":       { "type": "text"  },
        "source":     { "type": "keyword"  },
        "source_url": { "type": "keyword"  }, 
        "author":     { "type": "keyword"  },
        "facebook":   { "type": "integer" },
        "googleplus": { "type": "integer" },
        "linkedin":    { "type": "integer" },
        "published_at":{ "type": "date" },
        "permalink":   { "type": "keyword" },
        "canonical":   { "type": "keyword" },
        "candidate":   { "type": "keyword" }
      }
    }
  }
}
```