echo "Replacing Tag => 1...[python]"
mkdir js_python

echo "10k starting..."
mkdir js_python/10k
python3 -W ignore graph_clustering.py -n 10000 -t 0.5 --tag-list="[python]" > js_python/10k/result_10k_50.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.6 --tag-list="[python]" > js_python/10k/result_10k_60.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.65 --tag-list="[python]" > js_python/10k/result_10k_65.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.7 --tag-list="[python]" > js_python/10k/result_10k_70.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.75 --tag-list="[python]" > js_python/10k/result_10k_75.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.8 --tag-list="[python]" > js_python/10k/result_10k_80.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.85 --tag-list="[python]" > js_python/10k/result_10k_85.txt
python3 -W ignore graph_clustering.py -n 10000 -t 0.9 --tag-list="[python]" > js_python/10k/result_10k_90.txt
echo "10k completed..."

echo "20k starting..."
mkdir js_python/20k
python3 -W ignore graph_clustering.py -n 20000 -t 0.5 --tag-list="[python]" > js_python/20k/result_20k_50.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.6 --tag-list="[python]" > js_python/20k/result_20k_60.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.65 --tag-list="[python]" > js_python/20k/result_20k_65.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.7 --tag-list="[python]" > js_python/20k/result_20k_70.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.75 --tag-list="[python]" > js_python/20k/result_20k_75.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.8 --tag-list="[python]" > js_python/20k/result_20k_80.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.85 --tag-list="[python]" > js_python/20k/result_20k_85.txt
python3 -W ignore graph_clustering.py -n 20000 -t 0.9 --tag-list="[python]" > js_python/20k/result_20k_90.txt
echo "20k completed..."

echo "30k starting..."
mkdir js_python/30k
python3 -W ignore graph_clustering.py -n 30000 -t 0.5 --tag-list="[python]" > js_python/30k/result_30k_50.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.6 --tag-list="[python]" > js_python/30k/result_30k_60.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.65 --tag-list="[python]" > js_python/30k/result_30k_65.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.7 --tag-list="[python]" > js_python/30k/result_30k_70.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.75 --tag-list="[python]" > js_python/30k/result_30k_75.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.8 --tag-list="[python]" > js_python/30k/result_30k_80.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.85 --tag-list="[python]" > js_python/30k/result_30k_85.txt
python3 -W ignore graph_clustering.py -n 30000 -t 0.9 --tag-list="[python]" > js_python/30k/result_30k_90.txt
echo "30k completed..."

echo "40k starting..."
mkdir js_python/40k
python3 -W ignore graph_clustering.py -n 40000 -t 0.5 --tag-list="[python]" > js_python/40k/result_40k_50.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.6 --tag-list="[python]" > js_python/40k/result_40k_60.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.65 --tag-list="[python]" > js_python/40k/result_40k_65.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.7 --tag-list="[python]" > js_python/40k/result_40k_70.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.75 --tag-list="[python]" > js_python/40k/result_40k_75.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.8 --tag-list="[python]" > js_python/40k/result_40k_80.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.85 --tag-list="[python]" > js_python/40k/result_40k_85.txt
python3 -W ignore graph_clustering.py -n 40000 -t 0.9 --tag-list="[python]" > js_python/40k/result_40k_90.txt
echo "40k completed..."

echo "50k starting..."
mkdir js_python/50k
python3 -W ignore graph_clustering.py -n 50000 -t 0.5 --tag-list="[python]" > js_python/50k/result_50k_50.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.6 --tag-list="[python]" > js_python/50k/result_50k_60.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.65 --tag-list="[python]" > js_python/50k/result_50k_65.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.7 --tag-list="[python]" > js_python/50k/result_50k_70.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.75 --tag-list="[python]" > js_python/50k/result_50k_75.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.8 --tag-list="[python]" > js_python/50k/result_50k_80.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.85 --tag-list="[python]" > js_python/50k/result_50k_85.txt
python3 -W ignore graph_clustering.py -n 50000 -t 0.9 --tag-list="[python]" > js_python/50k/result_50k_90.txt
echo "50k completed..."