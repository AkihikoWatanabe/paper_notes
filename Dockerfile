FROM python:3.10-slim
RUN apt-get update && apt-get install -y ruby-full curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev nodejs graphviz graphviz-dev
RUN pip install requests tqdm pygraphviz networkx Pillow
RUN export GEM_HOME="$HOME/gems"
RUN export PATH="$HOME/gems/bin:$PATH"
RUN gem install jekyll bundler
RUN bundle install