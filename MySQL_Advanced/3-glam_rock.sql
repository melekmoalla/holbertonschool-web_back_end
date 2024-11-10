-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, IFNULL(
        YEAR(split) - YEAR(formed), YEAR(CURDATE()) - YEAR(formed)
    ) AS lifespan
FROM metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY lifespan DESC;