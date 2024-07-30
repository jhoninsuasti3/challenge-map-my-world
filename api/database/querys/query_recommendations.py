from sqlalchemy import text

query = text(
    """
    SELECT l.id AS location_id, c.id AS category_id
    FROM locations l
    JOIN categories c ON l.id = c.location_id
    LEFT JOIN (
        SELECT location_id, category_id
        FROM location_category_reviewed
        WHERE reviewed_at > NOW() - INTERVAL '30 DAY'
    ) AS reviewed ON l.id = reviewed.location_id AND c.id = reviewed.category_id
    WHERE reviewed.location_id IS NULL AND reviewed.category_id IS NULL

    LIMIT 10;
    """
)
#Optional ORDER BY RAND(), is most cost