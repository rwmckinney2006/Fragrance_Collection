CREATE TABLE fragrances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    size_ml INT,
    concentration VARCHAR(100),
    retail_price DECIMAL(10, 2),
    notes VARCHAR(300),
    season VARCHAR(100),
    image_path VARCHAR(500)
);

INSERT INTO fragrances (name, brand, size_ml, retail_price, notes, concentration, season, image_path) VALUES
('Paper (Expressive)', 'Commodity', 100, 155.00, 'Iso E super, Cedar, Sandalwood', 'Eau de Parfum', 'Spring', 'Images/Commodity Paper (Expressive).webp'),
('Spicebomb Extreme', 'Viktor & Rolf', 90, 155.00, 'Saffron, Cinnamon, Cumin, Bourbon Whiskey, Tabacoo, Vanilla', 'Eau de Parfum', 'Fall/Winter', 'Images/Spicebomb Extreme.webp'),
('Bleu de Chanel', 'Chanel', 100, 165.00, 'Grapefruit, Lemon, Mint, Pink Pepper, Ginger, Nutmeg, Jasmine, Iso E Super, Incense, Vetiver, Cedar, Sandalwood, Patchouli, Labdanum, White Musk', 'Eau de Parfum', 'All Seasons', 'Images/Bleu de Chanel EDP.jpg'),
('Side Effect', 'Initio', 50, 280.00, 'Rum, Tabacoo, Cinnamon, Saffron, Sandalwood, Hedione, Vanilla', 'Eau de Parfum', 'Fall/Winter', 'Images/Side Effect.jpg'),
('Y','Yves Saint Laurent', 100, 165.00, 'Apple, Ginger, Bergamot, Sage, Juniper Berries, Geranium, Amberwood, Tonka Bean, Cedar, Vetier, Olibanum', 'Eau de Parfum', 'All Seasons', 'Images/Y EDP.jpg'),
('Brighton (Custom)', 'Olfactory NYC', 50, 85.00, 'Lemon, Bergamot, White Tea, Sandalwood, Musk, Hinoki, Juniper', 'Eau de Parfum', 'Spring/Summer', 'Images/Brighton.webp'),
('Grand Soir', 'Maison Francis Kurkdjian', 35, 165.00, 'Spanish Labdanum, Orange, Lavender, Siam Benzoin, Amber, Vanilla, Tonka Bean, Musk, Cedar', 'Eau de Parfum', 'Winter', 'Images/Grand Soir.jpg'),
('Karst', 'Aesop', 50, 200.00, 'Juniper, Bergamot, Pink Pepper, Rosemary, Sage, Cumin, Vetiver, Cedar, Sandalwood', 'Eau de Parfum', 'Spring', 'Images/Karst.jpg'),
('Ingenious Ginger', 'Goldfield & Banks', 50, 140.00, 'Ginger Flower, Lemon, Bergamot, Mandarin Orange, Magnolia, Jasmine, Rose, Vanilla, Amber, Sandalwood, Cashmeran, Musk, Patchoulu', 'Eau de Parfum', 'Summer', 'Images/Ingenious Ginger.jpg'),
('O, Unknown', 'Imaginary Authors', 50, 115.00, 'Orris, Black Tea, Tea, Tolu Balsam, Sandalwood, Musk, Moss', 'Eau de Parfum', 'Winter', 'Images/O, Unknown.jpg'),
('French Defense', 'Mind Games', 100, 395.00, 'Black Cherry, Violet Leaves, Chamomile, Rose, Geranium, Mimosa, Amber, Blonde Woods, Cedarwood', 'Extrait de Parfum', 'Fall/Winter', 'Images/French Defense.jpg'),
('Ani X', 'Nishane', 50, 260.00, 'Lemon, Bergamot, Ginger, Melon, Cardamom, Water Notes, Pink Pepper, Green Apple, Black Currant, Lavendar, Patchouli, Sage, Rose, Vanilla, Sandalwood, Cashmere Wood, Cedar, Ambergris, White Musk', 'Extrait de Parfum', 'Fall/Winter', 'Images/Ani X.jpg');