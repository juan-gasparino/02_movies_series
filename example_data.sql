INSERT INTO movies_movie (title, genre, image_url, description, year, likes, release_at) VALUES
('The Shawshank Redemption', 'Drama', 'https://via.placeholder.com/150', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 1994, 200, NOW()),
('The Godfather', 'Crime', 'https://via.placeholder.com/150', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 1972, 250, NOW()),
('The Dark Knight', 'Action', 'https://via.placeholder.com/150', 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', 2008, 300, NOW()),
('Pulp Fiction', 'Crime', 'https://via.placeholder.com/150', 'The lives of two mob hitmen, a boxer, a gangster, and his wife intertwine in four tales of violence and redemption.', 1994, 180, NOW()),
('Forrest Gump', 'Drama', 'https://via.placeholder.com/150', 'The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.', 1994, 220, NOW());

INSERT INTO series_serie (title, genre, image_url, description, seasons, year, likes, first_episode, last_episode) VALUES
('Breaking Bad', 'Crime', 'https://via.placeholder.com/150', 'A high school chemistry teacher turned methamphetamine producer partners with a former student to secure his family\'s future.', 5, 2008, 350, NOW(), NOW()),
('Game of Thrones', 'Fantasy', 'https://via.placeholder.com/150', 'Nine noble families wage war against each other in order to gain control over the mythical land of Westeros.', 8, 2011, 400, NOW(), NOW()),
('Stranger Things', 'Sci-Fi', 'https://via.placeholder.com/150', 'When a young boy disappears, his mother, a police chief, and his friends must confront terrifying supernatural forces in order to get him back.', 4, 2016, 320, NOW(), NOW()),
('The Crown', 'Drama', 'https://via.placeholder.com/150', 'The gripping, decades-spanning inside story of Her Majesty Queen Elizabeth II and the Prime Ministers who shaped Britain\'s post-war destiny.', 6, 2016, 280, NOW(), NOW()),
('The Mandalorian', 'Action', 'https://via.placeholder.com/150', 'The travels of a lone bounty hunter in the outer reaches of the galaxy, far from the authority of the New Republic.', 3, 2019, 340, NOW(), NOW());