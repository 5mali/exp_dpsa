import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.interpolate import interpn
import numpy as np

def figplot(state_space_coverage, action_space_coverage):
    fig = plt.figure(figsize=(5,5))
    cmap = plt.get_cmap("tab20")
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    rect_hist_action = [left+1, bottom, width, height]

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)
    axHist_action = plt.axes(rect_hist_action)
    
    batt_state = state_space_coverage[:,0]
    henergy_state = state_space_coverage[:,1]
    
#     data , x_e, y_e = np.histogram2d( batt_state,  henergy_state, bins = 100)
#     z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , state_space_coverage , method = "splinef2d", bounds_error = False )
#     z = gaussian_kde(state_space_coverage.reshape(2,-1))(state_space_coverage.reshape(2,-1))
    
    
#     # Sort the points by density, so that the densest points are plotted last
#     idx = z.argsort()
#     batt_state, henergy_state, z = batt_state[idx], henergy_state[idx], z[idx]

    axScatter.scatter(batt_state,henergy_state,marker='.',s = 30, alpha=0.1, c=cmap(6));
    axScatter.set_xlabel("Battery")
    axScatter.set_ylabel("Harvested Energy")
#     plt.text(0.5,0.5,
#              s = r'$\sigma$'+" = "+ str(np.around(np.var(state_space_coverage), decimals=2)), 
#              transform = axScatter.transAxes)

    axScatter.set_xlim([0, 1])
    axScatter.set_ylim([0, 1])
    
    
    axHistx.hist(state_space_coverage[:,0],rwidth=1.0,bins=100,color=cmap(1),log=not False,histtype='step');
    axHistx.tick_params(labelbottom=False)
    axHistx.set_xlim([0, 1])


    axHisty.hist(state_space_coverage[:,1],bins=100,rwidth=1.0,orientation='horizontal',color=cmap(2),log=not False,histtype='step');
    axHisty.tick_params(labelleft=False)    
    axHisty.set_ylim([0, 1])


    axHist_action.hist(action_space_coverage,bins = 10,rwidth=0.95,color=cmap(0),log = not False)
    axHist_action.set_xlabel("Duty Cycle")
    axHist_action.yaxis.set_label_position("right")
    axHist_action.yaxis.tick_right()
    
    plt.show()
    
    return 0



def figplot3(state_space_coverage, action_space_coverage, explore_action_space_coverage):
    fig = plt.figure(figsize=(7,5))
    cmap = plt.get_cmap("tab20")
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    rect_hist_action = [left_h+0.3, bottom, width, height]
#     rect_xplr_action = [left_h+0.3+width+0.15,bottom, width, height]

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)
    axHist_action = plt.axes(rect_hist_action)
#     axExplr_action = plt.axes(rect_xplr_action)
    
    batt_state = state_space_coverage[:,0]
    henergy_state = state_space_coverage[:,1]
    
#     data , x_e, y_e = np.histogram2d( batt_state,  henergy_state, bins = 100)
#     z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , state_space_coverage , method = "splinef2d", bounds_error = False )
#     z = gaussian_kde(state_space_coverage.reshape(2,-1))(state_space_coverage.reshape(2,-1))
    
    
#     # Sort the points by density, so that the densest points are plotted last
#     idx = z.argsort()
#     batt_state, henergy_state, z = batt_state[idx], henergy_state[idx], z[idx]

    axScatter.scatter(batt_state,henergy_state,marker='.',s = 30, alpha=0.1, c=cmap(6));
    axScatter.set_xlabel("Battery", fontsize=14)
    axScatter.set_ylabel("Harvested Energy", fontsize=14)
#     plt.text(0.5,0.5,
#              s = r'$\sigma$'+" = "+ str(np.around(np.var(state_space_coverage), decimals=2)), 
#              transform = axScatter.transAxes)
    axScatter.set_xlim([0, 1])
    axScatter.set_ylim([0, 1])

    axHistx.hist(state_space_coverage[:,0],bins=100,color=cmap(1),log=not False,histtype='step');
    axHistx.tick_params(labelbottom=False)

    axHisty.hist(state_space_coverage[:,1],bins=100,orientation='horizontal',color=cmap(3),log=not False,histtype='step');        axHisty.tick_params(labelleft=False)

    axHist_action.hist([action_space_coverage],
                       label = ("Exploitive Actions"),
                       bins = 10,stacked=True,rwidth=0.95,
                       color=[cmap(0)],
                       log=not False)
    axHist_action.hist([explore_action_space_coverage],
                       label = ("Exploratory Actions"),
                       bins = 10,stacked=True,rwidth=0.95,
                       color=[cmap(2)],
                       log=not False)
        
    axHist_action.set_xlabel("Duty Cycle",fontsize=14)
    axHist_action.yaxis.set_label_position("right")
    axHist_action.yaxis.tick_right()
    axHist_action.legend(loc='upper center', bbox_to_anchor=(0.5, height+0.5), fancybox=True, shadow=True, ncol=2) 
    
#     axExplr_action.hist(explore_action_space_coverage,bins = 10,rwidth=0.95,color=cmap(4),log=not False)
#     axExplr_action.set_xlabel("Random Exploratory Duty Cycle")
# #     axExplr_action.yaxis.set_label_position("right")
# #     axExplr_action.yaxis.tick_right()
    
    plt.show()
    
    return 0

def scatter_only(state_space_coverage, action_space_coverage, explore_action_space_coverage):
    fig = plt.figure(figsize=(7,5))
    cmap = plt.get_cmap("tab20")
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.1

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
#     rect_histy = [left_h, bottom, 0.2, height]
#     rect_hist_action = [left+0.3, bottom, width, height]
# #     rect_xplr_action = [left_h+0.3+width+0.15,bottom, width, height]

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
#     axHisty = plt.axes(rect_histy)
#     axHist_action = plt.axes(rect_hist_action)
#     axExplr_action = plt.axes(rect_xplr_action)
    
    batt_state = state_space_coverage[:,0]
    henergy_state = state_space_coverage[:,1]
    
#     data , x_e, y_e = np.histogram2d( batt_state,  henergy_state, bins = 100)
#     z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , state_space_coverage , method = "splinef2d", bounds_error = False )
#     z = gaussian_kde(state_space_coverage.reshape(2,-1))(state_space_coverage.reshape(2,-1))
    
    
#     # Sort the points by density, so that the densest points are plotted last
#     idx = z.argsort()
#     batt_state, henergy_state, z = batt_state[idx], henergy_state[idx], z[idx]

    axScatter.scatter(batt_state,henergy_state,marker='.',s = 30, alpha=0.1, c=cmap(6));
    axScatter.set_xlabel("Battery", fontsize=14)
    axScatter.set_ylabel("Harvested Energy", fontsize=14)
#     plt.text(0.5,0.5,
#              s = r'$\sigma$'+" = "+ str(np.around(np.var(state_space_coverage), decimals=2)),
#              fontsize=14,
#              transform = axScatter.transAxes)


#     axHistx.hist(state_space_coverage[:,0],bins=100,color=cmap(1),log=not False,histtype='step');
#     axHistx.tick_params(labelbottom=False)

#     axHisty.hist(state_space_coverage[:,1],bins=100,orientation='horizontal',color=cmap(3),log=not False,histtype='step');        axHisty.tick_params(labelleft=False)

    axHistx.hist([action_space_coverage],
                       label = ("Exploitive Actions"),
                       bins = 10,stacked=True,rwidth=0.95,
                       color=[cmap(0)],
                       log=not False)
    axHistx.hist([explore_action_space_coverage],
                       label = ("Exploratory Actions"),
                       bins = 10,stacked=True,rwidth=0.95,
                       color=[cmap(2)],
                       log=not False)
        
    axHistx.set_xlabel("Duty Cycle",fontsize=14)
    axHistx.xaxis.set_label_position("top")
#     axHistx.yaxis.tick_right()
#     axHistx.legend(loc='upper right', 
# #                    bbox_to_anchor=(1, height), 
#                    fancybox=True, shadow=True, ncol=1) 
    
#     axExplr_action.hist(explore_action_space_coverage,bins = 10,rwidth=0.95,color=cmap(4),log=not False)
#     axExplr_action.set_xlabel("Random Exploratory Duty Cycle")
# #     axExplr_action.yaxis.set_label_position("right")
# #     axExplr_action.yaxis.tick_right()
    
    plt.show()
    fig.savefig('d9.pdf')
    return 0
