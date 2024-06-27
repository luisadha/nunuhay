<!DOCTYPE html>
<html>
<head>
    <title>CSV to HTML Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h2>CSV to HTML Table</h2>

<?php
$file = '/data/data/com.termux/files/home/nunuhay_data_total.csv'; // Path ke file CSV

// Periksa apakah file CSV ada
if (!file_exists($file) || !is_readable($file)) {
    echo "File tidak ditemukan atau tidak bisa dibaca.";
    exit;
}

// Buka file CSV
if (($handle = fopen($file, 'r')) !== FALSE) {
    echo '<table>';
    
    $isHeader = true;
    
    // Baca baris CSV satu per satu
    while (($row = fgetcsv($handle, 1000, ',')) !== FALSE) {
        echo '<tr>';
        
        // Buat header tabel dari baris pertama CSV
        if ($isHeader) {
            foreach ($row as $header) {
                echo '<th>' . htmlspecialchars($header) . '</th>';
            }
            $isHeader = false;
        } else {
            // Buat baris data dari baris CSV berikutnya
            foreach ($row as $data) {
                echo '<td>' . htmlspecialchars($data) . '</td>';
            }
        }
        
        echo '</tr>';
    }
    echo '</table>';
    
    fclose($handle);
} else {
    echo "Gagal membuka file.";
}
?>

</body>
</html>
