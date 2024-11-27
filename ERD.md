erDiagram
    USER {
        int id
        string username
        string password
        string email
        string phone_number
        string address
        string postcode
        date date_of_birth
    }
    SYNDICATE {
        int id
        string name
        int manager_id
    }
    MEMBER {
        int id
        string name
        string address
        string postcode
        string email
        string phone_number
        date date_of_birth
        int syndicate_id
    }
    MEMBERSHIP {
        int id
        int user_id
        int syndicate_id
        decimal percentage
        boolean participates_in_draws
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
        string line1_numbers
        string line2_numbers
    }
    TICKET {
        int id
        int draw_id
        int syndicate_id
        string ticket_number
        date purchase_date
    }

    USER ||--o{ SYNDICATE : manages
    USER ||--o{ MEMBERSHIP : is_member
    SYNDICATE ||--o{ MEMBERSHIP : has_member
    SYNDICATE ||--o| SYNDICATEAGREEMENT : has_agreement
    SYNDICATE ||--o{ TICKET : has_ticket
    LOTTERYDRAW ||--o{ TICKET : includes_ticket
    SYNDICATE ||--o{ MEMBER : includes_member
