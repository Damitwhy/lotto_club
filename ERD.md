erDiagram
    USER {
        int id
        string username
        string password
        string email
    }
    SYNDICATE {
        int id
        string name
        int manager_id
    }
    MEMBERSHIP {
        int id
        int user_id
        int syndicate_id
        decimal percentage
    }
    SYNDICATEAGREEMENT {
        int id
        int syndicate_id
        text agreement_text
        datetime created_at
    }
    LOTTERYDRAW {
        int id
        date date
        string draw_type
        string lottery_type
    }
    TICKET {
        int id
        int draw_id
        int syndicate_id
        string ticket_number
    }

    USER ||--o{ SYNDICATE : manages
    USER ||--o{ MEMBERSHIP : is_member
    SYNDICATE ||--o{ MEMBERSHIP : has_member
    SYNDICATE ||--o| SYNDICATEAGREEMENT : has_agreement
    SYNDICATE ||--o{ TICKET : has_ticket
    LOTTERYDRAW ||--o{ TICKET : includes_ticket
