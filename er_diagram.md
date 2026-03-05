# Vortex Gym — Entity Relationship Diagram

```mermaid
erDiagram
    users {
        UUID id PK
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR email UK
        VARCHAR password_hash
        VARCHAR role
        TIMESTAMP created_at
        BOOLEAN is_active
        VARCHAR phone
        TEXT address
        VARCHAR profile_photo_path
    }

    rooms {
        UUID id PK
        VARCHAR name
        INT total_capacity
    }

    membership_plans {
        UUID id PK
        VARCHAR name UK
        DECIMAL monthly_price
        BOOLEAN is_active
        VARCHAR category
        VARCHAR description
        INT discount_level
        UUID recurring_group_id
        VARCHAR recurring_day_of_week
        VARCHAR recurring_start_time
        INT duration_minutes
        UUID allocated_room_id FK
        INT allocated_seats
    }

    membership_plan_trainers {
        UUID plan_id PK_FK
        UUID trainer_id PK_FK
    }

    subscriptions {
        UUID id PK
        UUID user_id FK
        UUID plan_id FK
        VARCHAR billing_cycle
        VARCHAR status
        TIMESTAMP start_date
        TIMESTAMP end_date
        TIMESTAMP updated_at
    }


